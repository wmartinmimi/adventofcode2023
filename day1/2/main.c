#include <stdio.h>
#include <string.h>

int toInt(char *c) {
  int n = *c - 48;
  if (0 < n && n < 10) return n;
  if (strncmp("one"  , c, 3) == 0) return 1;
  if (strncmp("two"  , c, 3) == 0) return 2;
  if (strncmp("three", c, 5) == 0) return 3;
  if (strncmp("four" , c, 4) == 0) return 4;
  if (strncmp("five" , c, 4) == 0) return 5;
  if (strncmp("six"  , c, 3) == 0) return 6;
  if (strncmp("seven", c, 5) == 0) return 7;
  if (strncmp("eight", c, 5) == 0) return 8;
  if (strncmp("nine" , c, 4) == 0) return 9;
  return -1;
}

int main() {
  char ln[100];

  int i, j;
  int c1, c2;
  int sum = 0;
  for (int line = 0; line < 1000; line++) {
    fgets(ln, sizeof(ln), stdin);
    i = 0;
    j = strlen(ln) - 1;
    c1 = c2 = -1;
    while (c1 == -1) {
      c1 = toInt(ln + i);
      i++;
    }
    while (c2 == -1) {
      c2 = toInt(ln + j);
      j--;
    }
    sum += c1 * 10 + c2;
  }
  printf("%d\n", sum);
}
