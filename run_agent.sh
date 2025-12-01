#!/bin/bash

# 创建日志目录
LOG_DIR="plan_logs_withRAG/5"
mkdir -p $LOG_DIR

echo "开始执行 agent.py 5次..."
echo "日志将保存到 $LOG_DIR/ 目录"

# 执行5次
for i in {1..5}
do
    echo "=== 第 $i 次执行 ==="
    
    # 执行 agent.py 并将输出保存到临时文件
    python agent.py > temp_output_$i.txt 2>&1
    
    # 从临时文件中提取计划部分（更精确的提取）
    echo "=== 第 $i 次执行计划 ===" > $LOG_DIR/plan_$i.log
    
    # 使用awk提取从"生成的计划:"开始到空行之间的所有步骤行
    awk '/生成的计划:/{found=1; next} /^$/{if(found) exit} found' temp_output_$i.txt >> $LOG_DIR/plan_$i.log
    
    # 如果上面的方法没有提取到，尝试另一种方法
    if [ ! -s $LOG_DIR/plan_$i.log ] || [ $(wc -l < $LOG_DIR/plan_$i.log) -le 1 ]; then
        # 尝试提取包含"步骤"的行
        grep "步骤" temp_output_$i.txt > $LOG_DIR/plan_$i.log
    fi
    
    # 检查是否成功提取到计划
    if [ -s $LOG_DIR/plan_$i.log ] && [ $(wc -l < $LOG_DIR/plan_$i.log) -gt 1 ]; then
        echo "✅ 第 $i 次执行的计划已保存到 $LOG_DIR/plan_$i.log"
        
        # 显示提取的内容
        echo "提取的计划内容:"
        cat $LOG_DIR/plan_$i.log
        echo "-------------------"
    else
        echo "❌ 第 $i 次执行未找到计划输出"
        # 尝试其他提取方法
        echo "尝试其他提取方法..."
        sed -n '/生成的计划:/,/^$/p' temp_output_$i.txt | grep -v "生成的计划:" | grep -v "^$" > $LOG_DIR/plan_$i.log
        
        if [ -s $LOG_DIR/plan_$i.log ]; then
            echo "✅ 使用备用方法提取成功"
            cat $LOG_DIR/plan_$i.log
            echo "-------------------"
        else
            echo "未找到计划信息" > $LOG_DIR/plan_$i.log
        fi
    fi
    
    # 删除临时文件
    rm -f temp_output_$i.txt
    
    # 在每次执行之间添加延迟
    sleep 2
done

echo ""
echo "执行完成！所有计划日志已保存到 $LOG_DIR/ 目录"
echo "日志文件列表:"
ls -la $LOG_DIR/