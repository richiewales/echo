import React from 'react'

function PostItem({ post }) {
  return (
    <article className="post-item">
      <img src={post.profilePicture} alt={post.profile} className="post-item-pp" />
      <div>
        <div className="">
          <p className="post-item-user">{post.profile}</p>
          <p className="post-item-time">{post.postTimestamp}</p>
        </div>
        <p className="post-item-content">{post.postContent}</p>
      </div>
    </article>
  )
}

export default PostItem;