/* gdc sem erros */

int a;

/* teste de funcao com parametros e corpo sem declaracoes */
int gdc (int u, int v)
{
    /* teste de selecao, expressaes, return e chamada de funcao */
    if (v == 0) return u;
    else return gdc(v,u-u/v*v);
}

/* teste de funcao sem parametros e sem corpo */
int input(void)
{
}

/* teste de funcao com parametro e sem corpo */
void output(int x)
{
}

/* teste de funcao sem parametro e com corpo completo */
void main(void)
{

   /* teste de diferentes tipos de variaveis, incluindo vetor */
   int x;
   int y;
   int u;
   int v[10];

   /* chamadas de funcoes */
   x = input();
   y = input();
   output(gdc(x,y));

   a = 1;

   /* teste atribuicao e repeticao */
   u = 0;
   x = 1;
   while (x <= 10)
   {
      u = u * 2;  
      v[x] = u;
      x = x + 1; 
   }

   /* teste return simples */   
   return;

}
