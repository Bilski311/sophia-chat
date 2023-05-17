package com.bw.sophia.clients

import org.springframework.cloud.openfeign.FeignClient
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestPart
import org.springframework.web.multipart.MultipartFile
import org.springframework.http.MediaType

@FeignClient(name = "chatServiceClient", url = "\${chatServiceClient.url}")
interface ChatServiceClient {
    @PostMapping(value = ["/file"], consumes = [MediaType.MULTIPART_FORM_DATA_VALUE])
    fun sendFile(@RequestPart("file") file: MultipartFile): ResponseEntity<String>
}
