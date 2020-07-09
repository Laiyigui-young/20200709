#! /usr/bin/awk


BEGIN {
FS="[ ]";
}



{
  arr[len++]=$0;
}



END{
    qsort(arr,0,len);
    printfile(arr,len+1);
    exit 0;
}




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


function printfile(array,len,k)
{
     for(k=1;k<len;k++)
       {
         print array[k];
       }
}
