import React from 'react';
import { Link } from 'react-router-dom';

const BlogPost = ({ post }) => {
  return (
    <div>
      <h2>{post.title}</h2>
      <p>{post.content}</p>
      <div>
        {post.images.map((src, index) => (
          <img key={index} src={src} alt={`Post ${post.id} - ${index}`} width="100" />
        ))}
      </div>
      <Link to={`/post/${post.id}`}>Read more</Link>
    </div>
  )
}

export default BlogPost;