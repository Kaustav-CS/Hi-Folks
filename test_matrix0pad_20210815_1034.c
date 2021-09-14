#include<stdio.h>
int main()
{
int i,j,a,b,temp,B[9][6],k,l;
int A[9][6]=
{
		{03,03,89,73,23,34},
		{23,54,23,34,56,78},
		{89,32,53,64,745,98},
		{34,64,76,0,35,34},
		{36,96,54,25,83,75},
		{34,68,06,36,64,77},
		{35,68,35,15,74,86},
		{42,57,98,46,34,90},
		{45,35,0,25,0,0}
		    
};
printf("\tOriginal Matrix: \n");
for (i=0;i<9;i++)
{
	for (j=0;j<6;j++)
	{
		printf("  %02d ",A[i][j]);
	}
	printf("\n");
}
// Manipulatiom 
for (i=0;i<9;i++)
{
	for (j=0;j<6;j++)
	{
		B[i][j] = A[i][j];
	}
}
for(i=0;i<9;i++)
{
	for (j=0;j<6;j++){
		if (A[i][j] == 0)
			{
				a=i;
				b=j;
				for (k=0;k<9;k++)
					{
						for (l=0;l<6;l++)
							{
								B[k][b]=0;
								B[a][l]=0;
							}
					}
			}
		}
}
printf("\n\n\tModified  Matrix: \n");
for (i=0;i<9;i++)
{
	for (j=0;j<6;j++)
		{
			printf("  %3d ",B[i][j]);
		}
	printf("\n");
}
return 0;
}
