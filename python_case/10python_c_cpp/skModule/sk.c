
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int fac(int n)
{
   if(n<2)
     return 1;
   
   return n*fac(n-1);	//这是一个嵌套函数
}

char* reverse(char* s)
{
   char t, *p=s, *q=(s+(strlen(s)-1));
   while(s && (p<q))
   {
      //*的优先级大于 ++/--
      t=*p;
      *p++ = *q;
      *q-- = t;
   }

   return s;
}

int test(void)
//int main(void)
{
   char s[1024]={0};

   printf("4! == %d\n",fac(4));
   printf("8! == %d\n",fac(8));

   strcpy(s, "sk in gis");
   printf("reversing 'sk in gis', we get '%s'\n",reverse(s));

   return 0;   
}
