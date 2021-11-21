#include<stdio.h>
struct bank{
int no;
char name[20];
float bal;      
}b[20];

void get_data(struct bank[],int);
void display(struct bank[],int);
void withdraw(struct bank[],int);
void deposit(struct bank[],int);
void search(struct bank[],int);

void main(){
int n;    
printf("enter details");
get_data(b,2);
printf("choose\n");
printf("1.display 2.deposit 3.withdraw 4.search");
scanf("%d",&n); 
switch(n)
{
    case 1:
        display(b,2);
        break;
        
    case 2:
        withdraw(b,2);
        break;
    
    case 3:
        deposit(b,2);
        break;
    
    case 4:
        search(b,2);
        break;
    
    default:
        exit(1);
        
}    
}

void get_data(struct bank b[],int r)
{
    int i;
    for(i=1;i<=r;i++)
    {
    printf("enter no, name, bal");
    scanf("%d%s%f",&b[i].no,b[i].name,&b[i].bal);    
    }    
}

void display(struct bank b[], int r)
{
    int i;
    for(i=1;i<=r;i++)
    {
    printf("no: %d\n",b[i].no);
    printf("name: %s\n",b[i].name);
    printf("balance: %f\n",b[i].bal);    

    }
}   

void withdraw(struct bank b[], int r)
{
    int amt,key,i;
    printf("enter account number");
    scanf("%d",&key);
    for(i=1;i<=r;i++)
    {
        if(b[i].no==key)
        {  break;}
    }    
           printf("enter amt");
            scanf("%d",&amt);
            if(b[i].bal>amt){
            b[i].bal=b[i].bal-amt;
            printf("balance= %f",b[i].bal);    
            }
            else{
                printf("balance is insufficient");
            }
    
}

void deposit(struct bank b[], int r)
{
    int amt,key,i;
    printf("enter account number");
    scanf("%d",&key);
    for(i=1;i<=r;i++)
    {
        if(b[i].no==key)
        {  break;}
    }    
    printf("enter amt");
    scanf("%d",&amt);
    b[i].bal=b[i].bal+amt;
    printf("balance= %f",b[i].bal);
}

void search(struct bank b[], int r)
{
    int i,key;
    printf("enter customer account number");
    scanf("%d",&key);
    for(i=1;i<=r;i++){
        if(b[i].no==key)
        {
            printf("name: %s",b[i].name);
            printf("balance: %d",b[i].bal);
        }
        else{
            printf("not found");
        }
    }
    
}
