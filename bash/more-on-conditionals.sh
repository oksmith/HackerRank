#!/bin/bash
read X; read Y; read Z;
if [ "$X" -eq "$Y" ] && [ "$Y" -eq "$Z" ]; then
    echo "EQUILATERAL"
elif [ "$X" -eq "$Y" ] || [ "$Y" -eq "$Z" ] || [ "$Z" -eq "$X" ]; then
    echo "ICOSCELES"
else
    echo "SCALENE"
fi
