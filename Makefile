feature-test:
	coverage run --source='./tracks_sdk' -m behave ./features && coverage report