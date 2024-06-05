import React from 'react';
import { Link } from 'react-router-dom';

const Home = ({ posts }) => {
    return (
        <div>
            <Link to="/" className="home-btn">영화관</Link>
            <div className="post-list">
                {posts.map(post => (
                    <Link to={`/post/${post.id}`} key={post.id} className="post">
                        <img src={post.images[0]} alt={post.title} />
                        <p className="post-title">{post.title}</p>
                    </Link>
                ))}
            </div>
            <Link to="/new-post" className="new-post-btn">New Post</Link>
        </div>
    );
};

export default Home;