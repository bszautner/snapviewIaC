variable "render_api_key" {
  description = "Render.com API kulcs"
  type        = string
  sensitive   = true
}

variable "django_secret_key" {
  description = "Django SECRET_KEY"
  type        = string
  sensitive   = true
}

variable "db_name" {
  description = "PostgreSQL name"
  type        = string
  sensitive   = true
}

variable "db_user" {
  description = "PostgreSQL user"
  type        = string
  sensitive   = true
}

variable "db_password" {
  description = "PostgreSQL password"
  type        = string
  sensitive   = true
}

variable "db_host" {
  description = "PostgreSQL host"
  type        = string
  sensitive   = true
}

variable "db_port" {
  description = "PostgreSQL port"
  type        = string
  sensitive   = true
}

variable "app_debug" {
  description = "Application debug"
  type        = string
  sensitive   = true
}

variable "cloudinary_cloud_name" {
   description = "Cloudinary cloud name"
   type        = string
   sensitive   = true 
}
variable "cloudinary_api_key"    { 
   description = "Cloudinary api key"
   type        = string
   sensitive   = true 
}
variable "cloudinary_api_secret" {
   description = "Cloudinary api secret"
   type        = string
   sensitive   = true 
}