This repository contains a simple blog app using Python/Django.

I'm going to use it as a proof of concept for django applications running with docker compose.

### Usage

    # Create and log on the VM
    vagrant up
    vagrant ssh
    
    # Install production dependencies
    # You can also type make dev for development env
    make prod
    # Create and sync the DB.
    make sync
    Run the tests.
    make test app=app.blog
    Run the application
    make run

You can browse the blog on localhost:9500 using your favourite browser!
