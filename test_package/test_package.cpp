#include <ogg/ogg.h>
#include <stdio.h>

int main() {
  ogg_sync_state state;
  ogg_sync_init(&state);
  printf("Test OK\n");
  return 0;
}
