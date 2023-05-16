package com.bw.sophia.file
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestParam
import org.springframework.web.bind.annotation.RestController
import org.springframework.web.multipart.MultipartFile

@RestController
class FileUploadController {
    @PostMapping("/upload")
    fun handleFileUpload(@RequestParam("file") file: MultipartFile): ResponseEntity<String> {
        println(file.name)
        println(file.originalFilename)

        return ResponseEntity.ok("File uploaded successfully, filename: ${file.originalFilename}")
    }
}



