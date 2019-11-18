#include <stdio.h>
#include <string.h>

int main()
{
        char name[30];
        char color[30];
        char velocity[30];
        char ans1[30];
        char ans3[30];
        char ans11[] = "blu";
        char ans12[] = "e t";
        char ans13[] = "eam";
        char ans2[] = "red";
        char ans31[] = "24 ";
        char ans32[] = "mil";
        char ans33[] = "es ";
        char ans34[] = "per ";
        char ans35[] = "hour";

        strcpy(ans1, ans11);
        strncat(ans1, ans12, 3);
        strncat(ans1, ans13, 3);

        strcpy(ans3, ans31);
        strncat(ans3, ans32, 3);
        strncat(ans3, ans33, 3);
        strncat(ans3, ans34, 4);
        strncat(ans3, ans35, 4);

        printf("Stop! Who would cross the Bin of Death\n");
        printf("must answer me these questions three,\n");
        printf("ere the decrypted files they see.\n");
        printf("What is your name? ");
        gets(name,30,stdin);

        if (strcmp(name, ans1)) {
            printf("*Throws you over the bridge*\n");
            return 0;
        }

        printf("What is your favorite color? ");
        gets(color,30,stdin);
        if (strcmp(color, ans2)) {
            printf("*Throws you over the bridge*\n");
            return 0;
        }

        printf("What is the average airspeed velocity of an unladen European swallow? ");
        gets(velocity,30,stdin);
        if (strcmp(velocity, ans3)) {
            printf("*Throws you over the bridge*\n");
            return 0;
        }
/* ======================================================= */
        // RED TEAMER: ENTER THE DECRYPT KEY HERE
        char key[] = "SuperSecretKey";
/* ======================================================= */

        printf("Alright, here you go: %s\n", key);
        return 1;
}
