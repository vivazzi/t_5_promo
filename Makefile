load_demo_data:
	wget -P local https://vivazzi.pro/media/t_5_promo/db.tar.gz https://vivazzi.pro/media/t_5_promo/media.tar.gz

	docker cp local/db.tar.gz t_5_promo_core_dev:/t_5_promo_core/db.tar.gz
	docker compose -f ./t_5_promo_compose_dev/docker-compose.yml exec t_5_promo_core tar -xvf /t_5_promo_core/db.tar.gz -C /t_5_promo_core/
	docker compose -f ./t_5_promo_compose_dev/docker-compose.yml exec t_5_promo_core pipenv run python manage.py loaddata /t_5_promo_core/db.json
	docker compose -f ./t_5_promo_compose_dev/docker-compose.yml exec t_5_promo_core rm /t_5_promo_core/db.tar.gz /t_5_promo_core/db.json

	docker cp local/media.tar.gz t_5_promo_core_dev:/t_5_promo_core/media.tar.gz
	docker compose -f ./t_5_promo_compose_dev/docker-compose.yml exec t_5_promo_core tar -xvf /t_5_promo_core/media.tar.gz -C /t_5_promo_core/
	docker compose -f ./t_5_promo_compose_dev/docker-compose.yml exec t_5_promo_core rm /t_5_promo_core/media.tar.gz

	rm local/db.tar.gz local/media.tar.gz