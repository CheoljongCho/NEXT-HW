import React, { useEffect, useState } from 'react';
import { getPostsFromLocalStorage } from '../utils'; // 오타 수정
import BlogPost from './BlogPost';

const BlogList = () => {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        const posts = getPostsFromLocalStorage();
        setPosts(posts);
    }, []);

    return (
        <div>
            {posts.map(post => (
                <BlogPost key={post.id} post={post} />
            ))}
        </div>
    );
};

export default BlogList;