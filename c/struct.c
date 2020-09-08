#include <stdio.h>

struct Student{
    int no;
    char name[256];
};

struct User{ 
    int no;
    char *name;
};

void updateByValue(struct Student students[], char *name);
void updateByReference(struct Student strudents[], char *name );

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
    
    char name[3] = "abc";
    updateByValue(student, name);
    updateByReference(student, name);
}

void updateByValue(struct Student students[], char *name){
	int i = 0;
	for(i = 0; i < 3; i++){
	    strcpy(students[i].name, name);
		printf("updateByValue%3d:%3s ",students[i].no,students[i].name);
		if(i == 2)printf("\n");
	}
}

void updateByReference(struct Student *p, char *name){
    int i = 0;
    for(i = 0; i < 3; i++){
        strcpy((p+i)->name, name);
        printf("updateByReference%3d%3s ", (p+i)->no, (p+i)->name);
        if(i == 2)printf("\n");
    }
}