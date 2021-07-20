LDFLAGS = -lssl -lcrypto
CFLAGS = -Wall -O3 -fPIC -shared

TARGET = find_suffix_for_pow.so

$(TARGET): find_suffix_for_pow.c
	gcc $(CFLAGS) $^ -o $@ $(LDFLAGS)

clean:
	rm -f $(TARGET)
