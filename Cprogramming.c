#include <stdio.h>

int main() {
    int choice;

    printf("Select your Engineering Course: \n");
    printf("1. Computer Science Engineering\n");
    printf("2. Mechanical Engineering\n");
    printf("3. Electrical Engineering\n");
    printf("4. AIML Engineering\n");
    printf("Enter your choice (1-4): ");
    
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            printf("You have selected Computer Science Engineering.\n");
            break;
        case 2:
            printf("You have selected Mechanical Engineering.\n");
            break;
        case 3:
            printf("You have selected Electrical Engineering.\n");
            break;
        case 4:
            printf("You have selected Civil Engineering.\n");
            break;
        default:
            printf("Invalid choice! Please select a number between 1 and 4.\n");
    }

    return 0;
}
