
#include <stdio.h>
#include <stdlib.h>
typedef struct{
    int id;
    float value;

} Data;

int main(){

   Data *ptr = (Data *)malloc(sizeof(Data));

    ptr->id =1;
    ptr->value = 99.5;

    printf("id: %d , Value: %.2f\n",ptr->id, ptr->value);

    free(ptr);

    return 0;
}