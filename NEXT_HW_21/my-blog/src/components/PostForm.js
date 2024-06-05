import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { convertToBase64 } from '../utils';

const PostForm = ({ onSave }) => {
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');
    const [images, setImages] = useState([null, null, null]);
    const navigate = useNavigate();

    const handleImageChange = (index, file) => {
        const newImages = [...images];
        newImages[index] = file;
        setImages(newImages);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const base64Images = await Promise.all(images.map(img => img ? convertToBase64(img) : null));
            const post = {
                id: Date.now(),
                title,
                content,
                images: base64Images,
                comments: [],
            };
            onSave(post);
            setTitle('');
            setContent('');
            setImages([null, null, null]);
            navigate('/'); // 홈으로 리다이렉트
        } catch (error) {
            console.error('Error converting images to Base64', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Title" required />
            <textarea value={content} onChange={(e) => setContent(e.target.value)} placeholder="Content" required />
            {images.map((img, index) => (
                <input
                    key={index}
                    type="file"
                    onChange={(e) => handleImageChange(index, e.target.files[0])}
                />
            ))}
            <button type="submit">Save Post</button>
        </form>
    );
};

export default PostForm;