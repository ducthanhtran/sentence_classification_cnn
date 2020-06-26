HELL := /bin/bash
PERC := 10 # percentage of development and test data
.PHONY: data, data_movie_review

data: data_movie_review

data_movie_review:
	{ \
	mkdir -p ./data/movie_review/raw/extracted; \
	wget -N http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz -P ./data/movie_review/raw; \
	tar -xvzf./data/movie_review/raw/rt-polaritydata.tar.gz -C ./data/movie_review/raw/extracted; \
	mkdir -p ./data/movie_review/interim; \
	iconv -f CP1252 -t UTF-8 ./data/movie_review/raw/extracted/rt-polaritydata/rt-polarity.neg -o ./data/movie_review/interim/rt-polarity.neg.utf8; \
	iconv -f CP1252 -t UTF-8 ./data/movie_review/raw/extracted/rt-polaritydata/rt-polarity.pos -o ./data/movie_review/interim/rt-polarity.pos.utf8; \
	sed -i -e 's/^/0|||/' ./data/movie_review/interim/rt-polarity.neg.utf8; \
	sed -i -e 's/^/1|||/' ./data/movie_review/interim/rt-polarity.pos.utf8; \
	cat ./data/movie_review/interim/rt-polarity.neg.utf8 ./data/movie_review/interim/rt-polarity.pos.utf8 > ./data/movie_review/interim/all_data.utf8; \
	./shuf_seeded.sh ./data/movie_review/interim/all_data.utf8 | gzip > ./data/movie_review/interim/all_data.utf8.shuffled.gz; \
	lines=$$(zcat ./data/movie_review/interim/all_data.utf8.shuffled.gz | wc -l); \
	num_test_and_dev_lines=$$(awk -v lines="$$lines" 'BEGIN {printf("%.0f\n", lines/${PERC})}'); \
	doubled=$$(($$num_test_and_dev_lines*2)); \
	zcat ./data/movie_review/interim/all_data.utf8.shuffled.gz | head -n $$doubled | gzip > ./data/movie_review/interim/test_and_dev.gz; \
	zcat ./data/movie_review/interim/test_and_dev.gz | split -d -l $$num_test_and_dev_lines --verbose --filter='gzip > $$FILE.gz' - ./data/movie_review/interim/split-; \
	mv ./data/movie_review/interim/split-00.gz ./data/movie_review/interim/test.gz; \
	mv ./data/movie_review/interim/split-01.gz ./data/movie_review/interim/dev.gz; \
	zcat ./data/movie_review/interim/all_data.utf8.shuffled.gz | tail -n +$$(($$doubled+1)) | gzip > ./data/movie_review/interim/train.gz; \
	mkdir -p ./data/movie_review/final; \
	ln -sf ../interim/train.gz ./data/movie_review/final/train.gz; \
	ln -sf ../interim/test.gz ./data/movie_review/final/test.gz; \
	ln -sf ../interim/dev.gz ./data/movie_review/final/dev.gz; \
	}

clean:
	rm -rf ./data/
