#!/bin/bash
## From https://www.gnu.org/software/coreutils/manual/html_node/Random-sources.html#Random-sources
get_seeded_random()
{
    seed="${1}"
    openssl enc -aes-256-ctr -pass pass:"${seed}" -nosalt </dev/zero 2>/dev/null
}

shuf --random-source=<(get_seeded_random 2020) ${1}
