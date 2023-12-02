#include <stdio.h>
#include <string.h>

int toInt(char c) {
  int i = c - 48;
  if (0 < i && i < 10) return i;
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
      c1 = toInt(ln[i]);
      i++;
    }
    while (c2 == -1) {
      c2 = toInt(ln[j]);
      j--;
    }
    sum += c1 * 10 + c2;
  }
  printf("%d\n", sum);
}
