#! /usr/bin/awk


BEGIN {
FS="[ ]";
}



{
    if (ARGIND==1){  
    a[len1++]=$0;
    }
    if (ARGIND==2){
    b[len2++]=$0;
    }
}



END{
    qsort(a,0,len1);
    printf "数据a"
    printfile(a,len1+1);
    #printf "Lena:%5d\n",len1;

    qsort(b,0,len2);
    printf "数据b"
    printfile(b,len2+1);
    #printf "Lenb:%5d\n",len2;

    #交集求解
    i=0;
    j=0;
    k=0;
    while (i<length(a) && j<length(b)){
         if(a[i]<b[j]){
             i++;
         }
         else if(a[i]>b[j]){
             j++;
         }
         else{
             c[k]=a[i]
             i++;
             j++;
             k++;
                }
        }
     printf "交集结果";
     printfile(c,length(c));

    #并集求解
    i=0;
    j=0;
    k=0;
    while (i<length(a) && j<length(b)){
         if(a[i]<b[j]){
             d[k]=a[i];
             i++;
         }
         else if(a[i]>b[j]){
	     d[k]=b[j];
             j++;
         }
         else{
             d[k]=a[i]
             i++;
             j++;
         }
	 k++
    }
    #extend操作
    if (i==length(a)){
        for(t=j;t<length(b);t++){
	    d[k]=b[t];
	    k++;
	}
    }
    else{
        for(t=j;t<length(a);t++){
            d[k]=a[t];
            k++;
        }
    }
    printf "并集结果";
    printfile(d,length(d));

    #差集a-b求解
    i=0;
    j=0;
    k=0;
    while (i<length(a) && j<length(b)){
         if(a[i]<b[j]){
             e[k]=a[i];
             i++;
	     k++;
         }
         else if(a[i]>b[j]){
             j++;
         }
         else{
             i++;
             j++;
         }
    }
    #extend操作
    if (i<length(a)){
        for(t=i;t<length(a);t++){
            e[k]=a[t];
            k++;
        }
    }
    printf "差集a-b结果\n";
    #printf "Len:%5d\n",length(e);
    printfile(e,length(e));

    #差集b-a求解
    i=0;
    j=0;
    k=0;
    while (i<length(a) && j<length(b)){
         if(a[i]<b[j]){
             i++;
         }
         else if(a[i]>b[j]){
             f[k]=b[j];
   	     j++;
	     k++;
         }
         else{
             i++;
             j++;
         }
    }
    #extend操作
    if (j<length(b)){
        for(t=j;t<length(b);t++){
            f[k]=b[t];
            k++;
        }
    }
    #printf "Len:%5d\n",length(f);
    printf "差集a-b结果\n";
    printfile(f,length(f));
    exit 0;
}

#归并排序
function qsort(array , p , r , t , i ,x)
{
    if (p < r) {
        x=array[p];
        i = p;
        j = r+1;
        while(array[--j] > x );
        while(i < j) {

            t = array[i];
            array[i]=array[j];
            array[j]=t;

            while(array[++i] < x );
            while(array[--j] > x );

        }
        qsort(array, p , j);
        qsort(array, j + 1 , r);
    }

}

#数组输出
function printfile(array,len,k)
{
     for(k=0;k<len;k++)
       {
         print array[k];
       }
}
