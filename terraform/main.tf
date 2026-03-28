terraform {
   cloud {
    organization = "snapview-org"
    workspaces {
      name = "snapview"
    }
  }

  required_providers {
    render = {
      source  = "render-oss/render"
      version = "1.1.0"
    }
  }
}

provider "render" {
  api_key = var.render_api_key
  owner_id = "tea-d73q2j1r0fns73cm2tdg"
}

resource "render_postgres" "db" {
  name     = "snapview-db"
  plan     = "free"
  region   = "frankfurt"
  version  = "16"

  lifecycle {
    prevent_destroy = true
  }
}

resource "render_web_service" "app" {
  name   = "snapview-app"
  plan   = "free"
  region = "frankfurt"

  runtime_source = {
    docker = {
      repo_url = "https://github.com/bszautner/snapviewIaC"
      branch   = "main"
      auto_deploy = true
    }
  }

env_vars = {
    SECRET_KEY = {
      value = var.django_secret_key
    }
    DEBUG = {
      value = var.app_debug
    }
    DB_NAME = {
      value = var.db_name
    }
    DB_USER = {
      value = var.db_user
    }
    DB_PASSWORD = {
      value = var.db_password
    }
    DB_HOST = {
      value = var.db_host
    }
    DB_PORT = {
      value = var.db_port
    }
    CLOUDINARY_CLOUD_NAME = {
      value = var.cloudinary_cloud_name
    }
    CLOUDINARY_API_KEY = {
      value = var.cloudinary_api_key
    }
    CLOUDINARY_API_SECRET = {
      value = var.cloudinary_api_secret
    }
    LAST_DEPLOY = {
      value = "2026-03-22-v7" 
    }
  }
}