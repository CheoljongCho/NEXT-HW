import React, { useEffect, useState, useRef } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom'; // Link 추가
import CommentList from '../components/CommentList';
import CommentForm from '../components/CommentForm';

const Post = ({ posts, onUpdate, onDelete }) => {
    const { id } = useParams();
    const navigate = useNavigate();
    const [post, setPost] = useState(null);
    const [isEditing, setIsEditing] = useState(false);
    const [editTitle, setEditTitle] = useState('');
    const [editContent, setEditContent] = useState('');
    const imgRefs = useRef([]);

    useEffect(() => {
        if (posts && posts.length > 0) {
            const foundPost = posts.find(p => p.id === parseInt(id));
            if (foundPost) {
                setPost(foundPost);
                setEditTitle(foundPost.title);
                setEditContent(foundPost.content);
            }
        }
    }, [id, posts]);

    const handleImageClick = (index) => {
        const newImageUrl = prompt('Enter new image URL', post.images[index]);
        if (newImageUrl) {
            imgRefs.current[index].src = newImageUrl;
            const newImages = [...post.images];
            newImages[index] = newImageUrl;
            const newPost = { ...post, images: newImages };
            setPost(newPost);
            onUpdate(newPost);
        }
    };

    const addComment = (comment) => {
        const newComments = [...post.comments, comment];
        const newPost = { ...post, comments: newComments };
        setPost(newPost);
        onUpdate(newPost);
    };

    const deleteComment = (index) => {
        const newComments = post.comments.filter((_, i) => i !== index);
        const newPost = { ...post, comments: newComments };
        setPost(newPost);
        onUpdate(newPost);
    };

    const editComment = (index, newComment) => {
        const newComments = post.comments.map((comment, i) => (i === index ? newComment : comment));
        const newPost = { ...post, comments: newComments };
        setPost(newPost);
        onUpdate(newPost);
    };

    const handleDeletePost = () => {
        onDelete(post.id);
        navigate('/');
    };

    const handleEditPost = () => {
        const updatedPost = { ...post, title: editTitle, content: editContent };
        setPost(updatedPost);
        onUpdate(updatedPost);
        setIsEditing(false);
    };

    return (
      <div>
          <Link to="/" className="home-btn">영화관</Link> {/* 홈 버튼 추가 */}
          {post ? (
              <div>
                  {isEditing ? (
                      <div>
                          <input type="text" value={editTitle} onChange={(e) => setEditTitle(e.target.value)} />
                          <textarea value={editContent} onChange={(e) => setEditContent(e.target.value)} />
                          <button onClick={handleEditPost}>Save</button>
                          <button onClick={() => setIsEditing(false)}>Cancel</button>
                      </div>
                  ) : (
                      <div>
                          <h1>{post.title}</h1>
                          <p>{post.content}</p>
                          <button onClick={() => setIsEditing(true)}>Edit Post</button>
                      </div>
                  )}
                  <div>
                      {post.images.map((src, index) => (
                          <img
                              key={index}
                              ref={(el) => (imgRefs.current[index] = el)}
                              src={src}
                              alt={`Post ${post.id} - ${index}`}
                              width="200"
                              onClick={() => handleImageClick(index)}
                          />
                      ))}
                  </div>
                  <button onClick={handleDeletePost}>Delete Post</button>
                  <CommentList comments={post.comments} onDelete={deleteComment} onEdit={editComment} />
                  <CommentForm onAdd={addComment} />
              </div>
          ) : (
              <div>Loading...</div>
          )}
      </div>
  );
};

export default Post;