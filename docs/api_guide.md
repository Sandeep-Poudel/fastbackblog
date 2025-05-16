# API Guide

## Overview

This guide provides details on how to interact with the Blog API.

## Endpoints

### 1. Get All Blogs
- **URL**: `/blogs`
- **Method**: `GET`
- **Response**:
  ```json
  [
    {
      "id": 1,
      "title": "Sample Blog",
      "description": "This is a sample blog.",
      "author": "Author Name",
      "pic": "https://picsum.photos/seed/1234/600/400",
      "created_at": "2025-05-16T12:00:00",
      "updated_at": "2025-05-16T12:00:00"
    }
  ]
  ```

### 2. Create a New Blog
- **URL**: `/blogs`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "title": "New Blog",
    "description": "This is a new blog.",
    "author": "Author Name"
  }
  ```
- **Response**:
  ```json
  {
    "id": 2,
    "title": "New Blog",
    "description": "This is a new blog.",
    "author": "Author Name",
    "pic": "https://picsum.photos/seed/5678/600/400",
    "created_at": "2025-05-16T12:10:00",
    "updated_at": "2025-05-16T12:10:00"
  }
  ```

### 3. Get a Blog by ID
- **URL**: `/blog/{blog_id}`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "id": 1,
    "title": "Sample Blog",
    "description": "This is a sample blog.",
    "author": "Author Name",
    "pic": "https://picsum.photos/seed/1234/600/400",
    "created_at": "2025-05-16T12:00:00",
    "updated_at": "2025-05-16T12:00:00"
  }
  ```

### 4. Update a Blog
- **URL**: `/blog/{blog_id}`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
    "title": "Updated Blog Title",
    "description": "This is a sample blog.",
    "author": "Author Name"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "title": "Updated Blog Title",
    "description": "This is a sample blog.",
    "author": "Author Name",
    "pic": "https://picsum.photos/seed/1234/600/400",
    "created_at": "2025-05-16T12:00:00",
    "updated_at": "2025-05-16T12:15:00"
  }
  ```

### 5. Delete a Blog
- **URL**: `/blog/{blog_id}`
- **Method**: `DELETE`
- **Response**: `204 No Content`