import React from 'react'

function PostItem({ post }) {
  return (
    <article>
        <p>{post.profile}</p>
        <img src={post.profilePicture} alt={post.profile} />
        <p>{post.postContent}</p>
        <p>{post.postTimestamp}</p>
    </article>
  )
}

export default PostItem;