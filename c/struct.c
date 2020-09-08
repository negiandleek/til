#include <stdio.h>

struct Student{
    int no;
    char name[256];
};

struct User{ 
    int no;
    char *name;
};

void outputByValue(struct Student students[]);
void outputByReference(struct Student strudents[]);

int main(void){
    struct Student student[3] = {
        {1, "hoge"},
        {2, "fuga"},
        {3, "piyo"}
    };
    
    int i = 0;
    for(i = 0; i < 3; i++){
        printf("%3d:%4s", student[i].no, student[i].name);
        if(i == 2)printf("\n");
    }

    struct User users[3] = {
        {1, "foo"},
        {2, "bar"},
        {3, "baz"}
    };
    struct User *p;
    p = users;
    
    i = 0;
    for(i = 0; i < 3; i++){
        printf("%3d:%3s", (p+i)->no, (p+i)->name);
        if(i == 2)printf("\n");
    }
    
    outputByValue(student);
    outputByReference(student);
}

void outputByValue(struct Student students[]){
	int i = 0;
	for(i = 0; i < 3; i++){
		printf("outputByValue%3d:%3s",students[i].no,students[i].name);
		if(i == 2)printf("\n");
	}
}

void outputByReference(struct Student *p){
    int i = 0;
    for(i = 0; i < 3; i++){
        printf("outputByReference%3d%3s", (p+i)->no, (p+i)->name);
        if(i == 2)printf("\n");
    }
}
