const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

// 게시글 좋아요 ajax
const form = document.querySelector('#like-forms')
form.addEventListener('submit', function (event) {
  event.preventDefault()
  const postId = event.target.dataset.postId
  axios({
    method: "POST",
    url: `/posts/${postId}/likes/`,
    headers: {'X-CSRFToken': csrftoken},
  })
    .then((response) => {
      const isLiked = response.data.is_liked
      const likeBtn = document.querySelector(`#like--${postId}`)
      if (isLiked === true) {
        likeBtn.value = '좋아요 취소'
      } else {
        likeBtn.value = '좋아요'
      }
      // 좋아요 수 태그 
      const postLikeCountTag = document.querySelector('#post-like-count')
      // view 응답 json
      const postLikeCountData = response.data.post_like_count

      postLikeCountTag.textContent = postLikeCountData
    })
    .catch((error) => {
      console.log(error.response)
    })
})

