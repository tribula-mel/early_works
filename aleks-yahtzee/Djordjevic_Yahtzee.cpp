//Alex Djordjevic Yahtzee assignment

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <errno.h>

static bool firstDie = true;
static bool secondDie = true;
static bool thirdDie = true;
static bool fourthDie = true;
static bool fifthDie = true;

static void choose_die(char *die) {
    while (*(die++) != NULL) {
        switch(*die) {
        case '1':
            firstDie = true;
            break;
        case '2':
            secondDie = true;
            break;
        case '3':
            thirdDie = true;
            break;
        case '4':
            fourthDie = true;
            break;
        case '5':
            fifthDie = true;
            break;
        default:
            break;
        }
    }
}

int main (void) {

    char cont = 'y';
    char reroll[10] = "";
    int die1 = 0;
    int die2 = 1;
    int die3 = 2;
    int die4 = 3;
    int die5 = 4;
    int rollNum = 1;

    system("color a");

    printf("\n\n Welcome to my Yahtzee program!\n\n Enter y to continue:");
    fflush(stdin);
    fgets(&cont, sizeof(cont), stdin);

    srand(time(0));
    while(!(die1 == die2 && die2 == die3 && die3 == die4 && die4 == die5)) {
        if(firstDie){
            die1 = rand() % 6 + 1;
        }
        if(secondDie){
            die2 = rand() % 6 + 1;
        }
        if(thirdDie){
            die3 = rand() % 6 + 1;
        }
        if(fourthDie){
            die4 = rand() % 6 + 1;
        }
        if(fifthDie){
            die5 = rand() % 6 + 1;
        }
        firstDie = false;
        secondDie = false;
        thirdDie = false;
        fourthDie = false;
        fifthDie = false;

        printf("\nRoll %d: %3d %3d %3d %3d %3d\n", rollNum, die1, die2, die3, die4, die5);
        rollNum++;

        if (die1 == die2 && die2 == die3 && die3 == die4 && die4 == die5) {
            break;
        }

        printf("\nSelect the number of the die you wish to reroll(1-5):");
        fflush(stdin);
        bzero(&reroll, sizeof(reroll));
        fgets(&reroll[0], sizeof(reroll), stdin);
        choose_die(&reroll[0]);
    }
    printf("\n\nYahtzee!\n");
    return 0;
}
