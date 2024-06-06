import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Post from './pages/Post';
import PostForm from './components/PostForm';
import { getPostsFromLocalStorage, savePostsToLocalStorage } from './utils';
import './App.css'; // 스타일 파일 불러오기
import { Link } from 'react-router-dom';

const App = () => {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        const posts = getPostsFromLocalStorage();
        setPosts(posts);
    }, []);

    const handleSavePost = (post) => {
        const newPosts = [...posts, post];
        setPosts(newPosts);
        savePostsToLocalStorage(newPosts);
    };

    const handleUpdatePost = (updatedPost) => {
        const updatedPosts = posts.map(post => 
            post.id === updatedPost.id ? updatedPost : post
        );
        setPosts(updatedPosts);
        savePostsToLocalStorage(updatedPosts);
    };

    const handleDeletePost = (id) => {
        const updatedPosts = posts.filter(post => post.id !== id);
        setPosts(updatedPosts);
        savePostsToLocalStorage(updatedPosts);
    };

    return (
        <Router>
            <div className="container"> {/* 컨테이너 클래스 추가 */}
                <div className="title"> {/* 타이틀 클래스 추가 */}
                    <div className="title img">
                        <Link to="/" className="home-btn">영화관</Link> 
                    </div>
                </div>
                <Routes>
                    <Route path="/" element={<Home posts={posts} />} /> {/* 변경: Home 컴포넌트에 포스트 전달 */}
                    <Route 
                        path="/post/:id" 
                        element={<Post 
                            posts={posts} 
                            onUpdate={handleUpdatePost} 
                            onDelete={handleDeletePost} 
                        />} 
                    />
                    <Route 
                        path="/new-post" 
                        element={<PostForm onSave={handleSavePost} />} 
                    />
                </Routes>
            </div>
        </Router>
    );
};

export default App;