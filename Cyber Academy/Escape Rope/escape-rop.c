#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void win() {
    printf(
        "+=================+\n"
        "| You found an    |\n"
        "| escape rope in  |\n"
        "| your bag!      v|\n"
        "+=================+\n"
    );
    fflush(stdout);
    sleep(1);

    printf(
        "+=================+\n"
        "| There's a long  |\n"
        "| note attached   |\n"
        "| to it....      v|\n"
        "+=================+\n"
    );
    fflush(stdout);
    sleep(1);

    printf("%s\n", getenv("FLAG"));
    fflush(stdout);
}

void start_game() {
    // all possible item names are less than 11 chars for UI sizing
    char item_name[11];

    printf(
        "                   \n"
        "                  |\n"
        "        Magikarp  |\n"
        "             L1   |\n"
        "       HP:   1/ 20|\n"
        "      `___________/\n"
        "                   \n"
        "+======+==========+\n"
        "|      | FIGHT PM |\n"
        "|      |>ITEM RUN |\n"
        "+======+==========+\n"
        "                   \n"
        "Item > "
    );
    fflush(stdout);

    gets(&item_name);

    if (true) {
        printf(
            "+=================+\n"
            "| You don't have  |\n"
            "| any %-11s |\n"
            "| in your bag...  |\n"
            "+=================+\n",
            item_name
        );
        fflush(stdout);
        sleep(1);
    }

    printf(
        "                   \n"
        "                  |\n"
        "        Magikarp  |\n"
        "             L1   |\n"
        "       HP:   0/ 20|\n"
        "      `___________/\n"
        "                   \n"
        "+=================+\n"
        "| Magikarp        |\n"
        "| fainted!        |\n"
        "+=================+\n"
    );
    fflush(stdout);
}

int main() {
    start_game();
}
