package com.bw.sophia.file
import com.bw.sophia.clients.ChatServiceClient
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestParam
import org.springframework.web.bind.annotation.RestController
import org.springframework.web.multipart.MultipartFile

@RestController
class FileUploadController(private val chatServiceClient: ChatServiceClient) {
    @PostMapping("/upload")
    fun handleFileUpload(@RequestParam("file") file: MultipartFile): ResponseEntity<String> {
        chatServiceClient.sendFile(file)

        return ResponseEntity.ok("File uploaded successfully, filename: ${file.originalFilename}")
    }
}



