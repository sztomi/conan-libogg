#include <ogg/ogg.h>
#include <stdio.h>

int main() {
  ogg_packet packet;
  ogg_packet_clear(&packet);
  printf("Test OK\n");
  return 0;
}
