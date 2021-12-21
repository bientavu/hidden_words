help:
	@echo "\n============================================================================="
	@echo "reload-lambda | Update code on lambda"
	@echo "reload-layer | Update code on layer"


reload-lambda:
	-rm hidden_words.zip
	zip -r hidden_words.zip ./*
	aws lambda update-function-code --function-name hidden_words --zip-file fileb://hidden_words.zip --no-cli-pager


.DEFAULT_GOAL := help