#include <openssl/sha.h>
#include <string.h>
#include <stdio.h>

/** Find a suffix for the proof of work (PoW) of input data.
 * A suffix is a PoW, if the hex dump of the SHA1 hash of the concatenation of the input data and the suffix
 * starts with difficulty number of zeros.
 */
void find_suffix_for_pow(char *result, int max_suffix_length, const char *input_data, int difficulty, long counter, int delta)
{
    const unsigned long difficulty_mask =
        (1L << (difficulty / 2 * 8)) - 1 + difficulty % 2 * (0xf0L << (difficulty / 2 * 8));

    const int input_data_length = strlen(input_data);

    unsigned char data[input_data_length + max_suffix_length + 1];
    memcpy(data, input_data, input_data_length);

    char * const suffix = (char *)data + input_data_length;
    int suffix_length = 0;

    unsigned char hash[SHA_DIGEST_LENGTH];

    do {
        counter += delta;

        suffix_length = snprintf(suffix, max_suffix_length + 1, "%lx", counter);
        suffix_length = (suffix_length < max_suffix_length) ? suffix_length : max_suffix_length;

        SHA1(data, input_data_length + suffix_length, hash);

    } while (*(unsigned long *)hash & difficulty_mask);  // loop until hash starts with difficulty number of zeros

    memcpy(result, suffix, suffix_length);
}
