SHELL := /bin/bash

download_data: 
	source ./venv/bin/activate && \
        python src/data/movie_reviews.py && \
        python src/data/trec_questions.py

clean ::
	rm -rf ./data/
    
