#include <stdio.h>
#include <stdlib.h>
#include <regex.h>

static int check_filename(char *filename, char *regex_expression) {
    regex_t regex;

    regcomp(&regex, regex_expression, REG_EXTENDED | REG_NOSUB);
    int ret_val = regexec(&regex, filename, 0, NULL, 0);

    regfree(&regex);

    return ret_val != REG_NOMATCH;
}

static void write_instruction(FILE *file, char *instruction, int indent) {
    for (int i = 0; i < indent * 4; i++) {
        fprintf(file, " ");
    }

    fprintf(file, "%s\n", instruction);
}

static void convert(FILE *src, FILE *dst) {
    fprintf(dst, "#include <stdio.h>\n");
    fprintf(dst, "#include <stdlib.h>\n");
    fprintf(dst, "\n");
    fprintf(dst, "int main(int argc, char *argv[]) {\n");
    fprintf(dst, "    unsigned char *buffer = calloc(30000, sizeof(char));\n");
    fprintf(dst, "    unsigned char *ptr = buffer;\n");
    fprintf(dst, "\n");

    int c, indent = 1;

    while ((c = fgetc(src)) != EOF) {
        switch (c) {
            case '>':
                write_instruction(dst, "ptr++;", indent);
                break;
            case '<':
                write_instruction(dst, "ptr--;", indent);
                break;
            case '+':
                write_instruction(dst, "(*ptr)++;", indent);
                break;
            case '-':
                write_instruction(dst, "(*ptr)--;", indent);
                break;
            case '.':
                write_instruction(dst, "putchar(*ptr);", indent);
                break;
            case ',':
                write_instruction(dst, "*ptr = getchar();", indent);
                break;
            case '[':
                write_instruction(dst, "while (*ptr) {", indent++);
                break;
            case ']':
                write_instruction(dst, "}", --indent);
                break;

            default:
                break;
        }
    }

    fprintf(dst, "\n");
    fprintf(dst, "    free(buffer);\n");
    fprintf(dst, "    return 0;\n");
    fprintf(dst, "}");
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("%s: Missing operand\n", argv[0]);
        return EXIT_FAILURE;
    }

    if (!check_filename(argv[1], "[[:alnum:]]{1,20}.bf")) {
        printf("%s: %s: File not recognized\n", argv[0], argv[1]);
        return EXIT_FAILURE;
    }

    FILE *src, *dst;

    if ((src = fopen(argv[1], "r")) == NULL) {
        printf("%s: %s: No such file or directory\n", argv[0], argv[1]);
        return EXIT_FAILURE;
    }

    if (argc > 2) {
        if (!check_filename(argv[2], "[[:alnum:]]{1,20}.c")) {
            printf("%s: %s: File not recognized\n", argv[0], argv[2]);

            fclose(src);
            return EXIT_FAILURE;
        }

        dst = fopen(argv[2], "w");
    } else {
        dst = fopen("main.c", "w");
    }

    convert(src, dst);

    fclose(src);
    fclose(dst);

    return EXIT_SUCCESS;
}