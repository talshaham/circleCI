terraform {
  required_version = ">= 1.6"




  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

}

provider "aws" {
  region  = "eu-north-1"
  profile = "tal1"

}
