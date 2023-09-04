import React from 'react'

function PostItem({ post }) {
  return (
    <article className="post-item">
      <img src={post.fields.author[1]} alt={post.fields.author[0]} className="post-item-pp" />
      <div>
        <div className="">
          <p className="post-item-user">{post.fields.author[0]}</p>
          <p className="post-item-time">{post.fields.timestamp}</p>
        </div>
        <p className="post-item-content">{post.fields.post_text}</p>
      </div>
    </article>
  )
}

export default PostItem;