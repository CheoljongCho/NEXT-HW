import React from 'react';
import { Link } from 'react-router-dom';

const Home = ({ posts }) => {
    return (
        <div>
            <div className="post-list">
                {posts.map(post => (
                    <Link to={`/post/${post.id}`} key={post.id} className="post">
                        <div 
                            className="post-thumbnail"
                            style={{ backgroundImage: `url(${post.images[0]})` }}
                        />
                        <p className="post-title">{post.title}</p>
                    </Link>
                ))}
            </div>
            <Link to="/new-post" className="new-post-btn">New Post</Link>
        </div>
    );
};

export default Home;