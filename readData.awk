#运行前
BEGIN{
        for(i=0;i<ARGC;i++)
		{
			printf ARGV[i];
		}
	printf "\n"
}
#运行中
{
	if(ARGIND==1){	
	        sum1+=$1
        	a[NR]=$1
		printf "%5d\n",a[NR]		
	} 
	if(ARGIND==2){  
                sum2+=$1
                b[NR]=$1
                printf "%5d\n",b[NR]	              
        }	
}
#运行后
END{
	printf "Total1:%5d,Average2:%5.2f\n",sum1,sum1/NR
	printf "Total2:%5d,Average2:%5.2f\n",sum2,sum2/NR
}
