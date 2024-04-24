#!/bin/bash
#first 2012/6/
#second modify parralized
#2012/7/26 by LinBoxi

#echo "Please wait while finding empty nodes Of [node1 ... node48]"
#declare -a nodeloads
#for ((i=1;i<49;i++))
#do
#if [ $i -lt 10 ]; then
#  node=$(echo node0$i)
#else
#  node=$(echo node$i)
#fi
#ssh  -f node$i 'ps -eo comm,pid,pcpu --sort -pcpu' | tail -n +2 | awk   'BEGIN{ sum=0;}{sum+=$3} END {printf("%6s %6.1f\n",v1,sum)}' v1=$node  >> /tmp/cpu_usage.$$
#done
#echo
#echo sorted


#echo "Please wait while finding empty nodes Of [node1 ... node48]"

#declare -a nodeloads
for ((i=2;i<39;i++))
do
if [ $i -lt 10 ]; then
  node=$(echo node$i)
else
  node=$(echo node$i)
fi
#echo $node >>/tmp/cpu_usage.$$;
#ssh   $node 'ps -eo comm,pid,pcpu --sort -pcpu | tail -n +2|head -n 2'|awk 'BEGIN{print "'$node'"}{print $0}'   >> /tmp/cpu_usage.$$ &
ssh   $node 'ps -eo comm,pid,pcpu --sort -pcpu | tail -n +2|head -n 1'|awk '{print "'$node'," $1,",",$2,",",$3}'   >> /tmp/cpu_usage.$$ &
#echo >>/tmp/cpu_usage.$$
sleep 0.1
done
sleep 3
echo unsorted

#sort /tmp/cpu_usage.$$ -k 1
#echo
#echo sorted
#sort /tmp/cpu_usage.$$
cat /tmp/cpu_usage.$$
cat /tmp/cpu_usage.$$ >all_node.csv
rm -rf /tmp/cpu_usage.$$
