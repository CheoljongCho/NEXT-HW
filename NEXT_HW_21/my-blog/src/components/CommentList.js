import React from 'react';

const CommentList = ({ comments, onDelete, onEdit }) => {
    if (!comments || comments.length === 0) {
        return <div>No comments yet.</div>;
    }

    return (
        <ul>
            {comments.map((comment, index) => (
                <li key={index}>
                    <p>{comment}</p>
                    <button onClick={() => onDelete(index)}>Delete</button>
                    <button onClick={() => {
                        const newComment = prompt('Edit comment', comment);
                        if (newComment) onEdit(index, newComment);
                    }}>Edit</button>
                </li>
            ))}
        </ul>
    );
};

export default CommentList;