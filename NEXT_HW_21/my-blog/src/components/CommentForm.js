import React, { useState } from 'react';

const CommentForm = ({ onAdd }) => {
    const [comment, setComment] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        onAdd(comment);
        setComment('');
    };

    return (
        <form onSubmit={handleSubmit}>
            <textarea value={comment} onChange={(e) => setComment(e.target.value)} />
            <button type="submit">Add Comment</button>
        </form>
    );
};

export default CommentForm;