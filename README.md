# t_5_promo

This is a small test application with stack:

- Django

You can find a task description in this repo: [docs/task_ru.md](docs/task_ru.md) (in Russian)

## Installing

1. Clone this project:

    ```shell
    git clone https://github.com/vivazzi/t_5_promo.git
    ```
   

## Running

### Development

1. Copy all files with environment variables from [t_5_promo_compose_dev/samples](t_5_promo_compose_dev/samples) to 
   [t_5_promo_compose_dev](t_5_promo_compose_dev) without `.sample` suffixes and set values.

2. Run:

   ```shell
   docker compose -f ./t_5_promo_compose_dev/docker-compose.yml up --build -d
   ```

3. (optionally) Apply migrations:

   ```shell
   docker compose -f ./t_5_promo_compose_dev/docker-compose.yml exec t_5_promo_core pipenv run python manage.py migrate
   ```

4. (optionally) Load demo data:

   ```shell
   make load_demo_data
   ```

5. (optionally) Create superuser, if you did not load demo data:

   ```shell
   docker compose -f ./t_5_promo_compose_dev/docker-compose.yml exec t_5_promo_core pipenv run python manage.py createsuperuser
   ```

6. Run in your browser http://localhost:8000/promo/


### Production

Not supported.

> **Warning**  
> Don't use development settings in production: it is not safe and optimally!


## Note

1. According to the task, all clickable elements has hover effect, but mockup does not consists necessary instructions.
So hover styles have been added by myself with `fixme: warning: inconsistent style` warning comment. 

2. All images have not been compressed (except for the images: bg in photos block)


## What can be improved?

1. Add component variants to mockup for hover, focus effects and so on. Now developer has to define hover effects by himself.
2. Mockup does not have the display of expanded menu in mobile version, so mobile menu button is not active.
3. Maybe add Slider Model with some reversion_id, that can use as unique identifier for the inserting to any place at page?
4. It would be nice to have a sample code (python, html, css, js and so on) to match the company's uniform coding style.
5. Overall, the layout could be improved: remove useless styles, add additional auto layouts, remove useless guides in the layout.
6. Maybe add django-sekizai package to task for better management js and css files?
